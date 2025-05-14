import base64
import binascii
import io
import logging
import mimetypes
from collections.abc import Sequence

import pdfplumber
import requests
from absl import app
from google.cloud import storage
from google.adk.tools import ToolContext
from google.genai.types import Blob, Part

logger = logging.getLogger(__name__)

async def download_file_from_url(
    uri: str, output_filename: str, tool_context: ToolContext
) -> str:
    """Downloads a file from a URL and stores it in an artifact.

    Args:
      url: The URL to retrieve the file from.
      output_filename: The name of the artifact to store the file in.
      tool_context: The tool context.

    Returns:
      The name of the artifact.
    """
    try:
    
        path_part = uri[len("gs://"):]
        # Split only on the first '/' to separate bucket from the rest
        bucket_name, blob_name = path_part.split('/', 1)

        # Initialize GCS client
        storage_client = storage.Client()

        # Get the bucket and blob objects
        bucket = storage_client.bucket(bucket_name)
        print(f"Bucket: {bucket}")
        blob = bucket.blob(blob_name)
        
        file_bytes = base64.b64encode(blob.download_as_bytes())
        

        parts = uri.rsplit('/', 1)
        filename = parts[-1]

        mime_type, encoding = mimetypes.guess_type(filename)       

        artifact = Part(inline_data=Blob(data=file_bytes, mime_type=mime_type))
        await tool_context.save_artifact(filename=output_filename, artifact=artifact)
        logger.info("Downloaded %s to artifact %s", uri, output_filename)
        return output_filename

    except requests.exceptions.RequestException as e:
        logger.error("Error downloading file from URL: %s", e)
        return None


async def extract_text_from_pdf_artifact(
    pdf_path: str, tool_context: ToolContext
) -> str:
    """Extracts text from a PDF file stored in an artifact"""
    pdf_artifact = await tool_context.load_artifact(pdf_path)
    try:
        with io.BytesIO(
            base64.b64decode(pdf_artifact.inline_data.data)
        ) as pdf_file_obj:
            pdf_text = ""
            with pdfplumber.open(pdf_file_obj) as pdf:
                for page in pdf.pages:
                    pdf_text += page.extract_text()
            return pdf_text
    except binascii.Error as e:
        logger.error("Error decoding PDF: %s", e)
        return None
    
def main(argv: Sequence[str]) -> None:
    if len(argv) > 1:
        raise app.UsageError("Too many command-line arguments.")


if __name__ == "__main__":
    app.run(main)