from docling.document_converter import DocumentConverter, PdfFormatOption
import os
import sys
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.datamodel.base_models import InputFormat
from docling_core.types.doc import ImageRefMode

# Set up pipeline options
pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = 2.0  # Optional: for higher resolution images
pipeline_options.generate_page_images = True
pipeline_options.generate_picture_images = True


def convert_local_pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert a local PDF file to markdown using Docling.
    
    Args:
        pdf_path (str): Path to the local PDF file
        output_path (str, optional): Path to save the markdown output
    
    Returns:
        str: The markdown content
    """
    # Check if the file exists
    if not os.path.exists(pdf_path):
        print(f"Error: The file '{pdf_path}' does not exist.")
        return None
    
    # Initialize the converter
    # Create converter
    converter = DocumentConverter(
        format_options={
            InputFormat.PDF: PdfFormatOption(
                pipeline_options=pipeline_options,
            )
        }
    )
    
    try:
        # Convert the document
        result = converter.convert(pdf_path)
        
        # Get the markdown content
        markdown_content = result.document.export_to_markdown()
        
        pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
        # Create output directory with PDF name
        output_dir = os.path.join("output", pdf_name)
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, "output.md")

        result.document.save_as_markdown(
            output_path,
            image_mode=ImageRefMode.REFERENCED
        )


        return markdown_content
    
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return None

if __name__ == "__main__":
    # Get the PDF path from command line arguments or use default
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = "./sample-pdfs/sample.pdf"  # Default local PDF file
    
    
    # Convert PDF to markdown
    print(f"Converting local PDF '{pdf_path}' to markdown...")
    markdown_content = convert_local_pdf_to_markdown(pdf_path)
    
    # Print a preview of the markdown content
    if markdown_content:
        print("\nMarkdown Preview:")
        preview = markdown_content[:500] + "..." if len(markdown_content) > 500 else markdown_content
        print(preview)
