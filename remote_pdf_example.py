from docling.document_converter import DocumentConverter
import os

def convert_pdf_to_markdown(pdf_path, output_path=None):
    """
    Convert a PDF file to markdown using Docling.
    
    Args:
        pdf_path (str): Path to the PDF file or URL
        output_path (str, optional): Path to save the markdown output
    
    Returns:
        str: The markdown content
    """
    # Initialize the converter
    converter = DocumentConverter()
    
    # Convert the document
    result = converter.convert(pdf_path)
    
    # Get the markdown content
    markdown_content = result.document.export_to_markdown()
    
    # Save to file if output_path is provided
    if output_path:
        # Create output directory if it doesn't exist
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(markdown_content)
        print(f"Markdown saved to {output_path}")
    
    return markdown_content

if __name__ == "__main__":
    # Example usage with a sample PDF
    # You can use a local file or a URL
    # pdf_path = "https://arxiv.org/pdf/2408.09869"  # Docling's own paper as an example
    pdf_path = "https://arxiv.org/pdf/2501.17887" # a report that includes docling
    
    # Extract PDF name from path or URL
    pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
    
    # Create output directory with PDF name
    output_dir = os.path.join("output", pdf_name)
    os.makedirs(output_dir, exist_ok=True)
    output_path = os.path.join(output_dir, "output.md")
    
    # Convert PDF to markdown
    print(f"Converting {pdf_path} to markdown in {output_path}")
    markdown_content = convert_pdf_to_markdown(
        pdf_path, 
        output_path=output_path
    )
    
    # Print a preview of the markdown content
    print("\nMarkdown Preview:")
    print(markdown_content[:500] + "..." if len(markdown_content) > 500 else markdown_content)
