# Installation Instructions

There are two ways of running ScholarVista. If you want to run the CLI in you system, you can install ScholarVista from source. If you want to run the

## From Source

To install **ScholarVista** from source, you can clone the repository and install the package using **_pip_**.

```bash
git clone https://github.com/mciccale/ScholarVista
cd ScholarVista
pip install .
```

When using **_pip_** it is a good practice to use virtual environments. Check out the official documentation on virtual envornments [here](https://docs.python.org/3/library/venv.html).

## Docker Container

1. **Ensure Prerequisites:**
   - Docker is installed on your system. If not, follow the instructions to install Docker from [here](https://docs.docker.com/get-docker/).
   - Ensure the other container that your CLI tool needs to communicate with is running and accessible on port 8080.

2. **Create a Docker Network:**
   - Create a Docker network to allow communication between containers.
     ```bash
     docker network create my-network
     ```

3. **Run the Other Container:**
   - Start the other container that your CLI tool needs to communicate with and attach it to the created Docker network.
     ```bash
     docker run -d --name other-container --network my-network -p 8080:8080 <other-container-image>
     ```
     Replace `<other-container-image>` with the image name or ID of the other container.

4. **Build the CLI Tool Docker Image:**
   - Clone the repository containing your CLI tool and navigate into its directory.
     ```bash
     git clone https://github.com/your-username/your-cli-tool
     cd your-cli-tool
     ```
   - Build the Docker image for your CLI tool.
     ```bash
     docker build -t my-scholarvista .
     ```

5. **Run the CLI Tool Docker Container:**
   - Run the Docker container for your CLI tool, ensuring it's connected to the same network as the other container.
     ```bash
     docker run -it --rm --network my-network -e INPUT_DIR="/path/to/input" -e OUTPUT_DIR="/path/to/output" my-scholarvista
     ```
     Replace `/path/to/input` and `/path/to/output` with the desired paths.

6. **Usage:**
   - Your CLI tool is now running within the Docker container and is able to communicate with the other container on port 8080. You can interact with your CLI tool as needed, providing input files in the specified input directory and accessing output files in the specified output directory.


