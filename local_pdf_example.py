from docling.document_converter import DocumentConverter
import os
import sys

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
    converter = DocumentConverter()
    
    try:
        # Convert the document
        result = converter.convert(pdf_path)
        
        # Get the markdown content
        markdown_content = result.document.export_to_markdown()
        
        # Save to file if output_path is provided
        if output_path:
            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(markdown_content)
            print(f"Markdown saved to {output_path}")
        
        return markdown_content
    
    except Exception as e:
        print(f"Error converting PDF: {e}")
        return None

if __name__ == "__main__":
    # Get the PDF path from command line arguments or use default
    if len(sys.argv) > 1:
        pdf_path = sys.argv[1]
    else:
        pdf_path = "sample.pdf"  # Default local PDF file
    
    # Set output path
    output_path = "local_output.md"
    
    # Convert PDF to markdown
    print(f"Converting local PDF '{pdf_path}' to markdown...")
    markdown_content = convert_local_pdf_to_markdown(pdf_path, output_path)
    
    # Print a preview of the markdown content
    if markdown_content:
        print("\nMarkdown Preview:")
        preview = markdown_content[:500] + "..." if len(markdown_content) > 500 else markdown_content
        print(preview)
