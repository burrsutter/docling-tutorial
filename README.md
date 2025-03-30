# Docling Tutorial


## Installation

```bash
python3.11 -m venv venv
source venv/bin/activate
```

To use Docling, simply install it using pip:

```bash
pip install docling
```

Docling works on macOS, Linux, and Windows environments, supporting both x86_64 and arm64 architectures.


## Usage Examples

This repository contains several examples of using Docling:

### 1. Python API Example

The `remote_pdf_example.py` script demonstrates how to use Docling's Python API to convert a PDF to markdown:

```bash
python remote_pdf_example.py
```

This will:
1. Download and process the PDF from the provided URL
2. Convert it to markdown
3. Save the output to `output.md`
4. Print a preview of the markdown content

### 2. Local PDF Example

The `local_pdf_example.py` script demonstrates how to use Docling with a local PDF file

```bash
python local_pdf_example.py sample-pdfs/hello_world.pdf
```

review local_output.md

```bash
python local_pdf_example.py sample-pdfs/Zippity_Zoo.pdf
```

review local_output.md

```bash
python local_pdf_example.py sample-pdfs/sales-summary.pdf
```


If no path is provided, it will look for a file named `sample.pdf` in the current directory.

### 3. CLI Example

Docling also provides a convenient command-line interface. The `cli_example.sh` script demonstrates how to use it:

```bash
# Basic usage
docling https://arxiv.org/pdf/2408.09869


# Using SmolDocling VLM (if available)
docling --pipeline vlm --vlm-model smoldocling https://arxiv.org/pdf/2408.09869 

docling --pipeline vlm --vlm-model smoldocling https://arxiv.org/pdf/2206.01062
```

For more details, check out the [advanced usage options](https://github.com/docling-project/docling) in the official documentation.

### 4. Text to PDF

```bash
brew install pandoc
brew install basictex
export PATH="/Library/TeX/texbin:$PATH"
```

```bash
pdflatex --version
```

```
pdfTeX 3.141592653-2.6-1.40.27 (TeX Live 2025)
kpathsea version 6.4.1
Copyright 2025 Han The Thanh (pdfTeX) et al.
There is NO warranty.  Redistribution of this software is
covered by the terms of both the pdfTeX copyright and
the Lesser GNU General Public License.
For more information about these matters, see the file
named COPYING and the pdfTeX source.
Primary author of pdfTeX: Han The Thanh (pdfTeX) et al.
Compiled with libpng 1.6.46; using libpng 1.6.46
Compiled with zlib 1.3.1; using zlib 1.3.1
Compiled with xpdf version 4.04
```

```bash
pandoc sample_text.txt -o sample.pdf
```

Then convert from PDF to .md

```bash
python local_pdf_example.py sample.pdf
```

## Docling Server


### API Server

```
pip install docling-serve
```

```
export DOCLING_MODELS_DIR="/Users/bsutter/ai-projects/docling-tutorial/docling_models"
```

```
docling-serve run
```

```
open http://127.0.0.1:5001/docs
```

```
curl -X 'POST' \
  'http://localhost:5001/v1alpha/convert/source' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
    "http_sources": [{"url": "https://arxiv.org/pdf/2501.17887"}]
  }'
```

### GUI

Stop the API server (control-c)

```
pip install "docling-serve[ui]"
```

```
docling-serve run --enable-ui
```

```
open http://127.0.0.1:5001/ui
```

And try some of the sample PDFs

![docling serve GUI 1](./screenshots/docling-serve-gui-1.png)

![docling serve GUI 2](./screenshots/docling-serve-gui-2.png)

![docling serve GUI 3](./screenshots/docling-serve-gui-3.png)


## Resources

- [Docling GitHub Repository](https://github.com/docling-project/docling)
- [Detailed Installation Instructions](https://github.com/docling-project/docling)
- [SmolDocling](https://github.com/docling-project/docling) - Visual Language Model for document understanding
