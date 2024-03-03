# Base image with 3.12 python
FROM python:3.12-slim

# Set the WD to scholarvista
WORKDIR /scholarvista

# Copy the source files
COPY . /scholarvista

# Install the package from source
RUN pip install .

# The entrypoint of the Docker Container will be the command with the dirs flags, we assume that the user will mount its dirs in the /input and /output lcations
ENTRYPOINT ["scholarvista", "--input-dir", "/input", "--output-dir", "/output"]

# Default command
CMD ["process-pdfs"]
