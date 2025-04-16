from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import DocumentConverter, PdfFormatOption
from docling_core.types.doc import ImageRefMode
import os
# Set up pipeline options
pipeline_options = PdfPipelineOptions()
pipeline_options.images_scale = 2.0  # Optional: for higher resolution images
pipeline_options.generate_page_images = True
pipeline_options.generate_picture_images = True

# Create converter
converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(
            pipeline_options=pipeline_options,
        )
    }
)

pdf_path = "https://arxiv.org/pdf/2501.17887"

# Convert document
result = converter.convert(pdf_path)


pdf_name = os.path.splitext(os.path.basename(pdf_path))[0]
# Create output directory with PDF name
output_dir = os.path.join("output", pdf_name)
os.makedirs(output_dir, exist_ok=True)
output_path = os.path.join(output_dir, "output.md")


# Save with referenced images
result.document.save_as_markdown(
    output_path,
    image_mode=ImageRefMode.REFERENCED
)

# Or save as HTML with referenced images
# output_path = os.path.join(output_dir, "output.html")
# result.document.save_as_html(
#     "output.html",
#     image_mode=ImageRefMode.REFERENCED
# )