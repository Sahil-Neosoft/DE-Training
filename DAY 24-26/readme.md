# Dockerized FastAPI E-commerce Application

This project described the containerization of a FastAPI-based E-commerce application using Docker. It covered Docker fundamentals, architecture, and practical implementation, including the creation of Dockerfiles, use of Docker Compose, and debugging within remote containers.

---

## Docker Basics & Architecture

Docker was used to create isolated, consistent environments for application deployment across different systems. The architecture involved several components:

- The Docker Engine managed the lifecycle of containers and provided the core runtime.
- Docker Images served as the blueprint for containers, containing application code and all dependencies.
- Containers, which were instances of images, executed the application in isolated environments.
- Docker Hub acted as a public registry for sharing and retrieving container images.

This setup ensured reproducibility and portability across various environments, reducing inconsistencies between development and production systems.

---

## Dockerfile, Docker Compose, and Docker Image

A Dockerfile had been created to define the environment and installation instructions needed to build the container image. It specified the application dependencies, working directory, and the default command to run the server.

The Docker image was then built from this Dockerfile. It packaged the application along with its runtime configuration, making it deployable on any machine with Docker installed.

Docker Compose was used to define and manage multi-container setups. The application and its supporting services, such as the database, were defined as individual services in a Compose file. This allowed the entire application stack to be brought up or torn down with a single command.

This approach enabled efficient orchestration, simplified configuration management, and clearer service separation.

---

## Running the FastAPI Application on Docker

The FastAPI application was containerized and run using Docker. The process included building the image, starting the container, and exposing the application through a specific port for access via a web browser or API client.

Docker Compose further simplified this by allowing all components — including the backend server and the database — to start together as a single application stack.

Once deployed, the application’s API endpoints were accessible through the browser, and interactive documentation was made available via auto-generated interfaces.

---

## Remote Container & Debugging of Applications

Remote Containers and Visual Studio Code were used to develop and debug the application directly inside a Docker container.

The development container setup included the necessary tools, dependencies, and configurations required for Python development. It allowed developers to work inside a fully reproducible environment without installing anything on the host machine.

Debugging was performed seamlessly by attaching the debugger to the running application inside the container. Developers were able to set breakpoints, inspect variables, and perform live edits, all while the application continued to run in isolation.

This setup ensured consistent behavior across team members and streamlined the debugging process.

---