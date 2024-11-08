# 📸 Snap Up - Django AWS Image Uploader 📸

## About the Project 🤖

**Snap Up** is a Django-based image uploader that allows users to easily upload images directly to an AWS S3 bucket. The project provides a simple, user-friendly interface for users to upload and display images on the website, ensuring the images are securely stored and accessible from anywhere, at any time. The integration with AWS S3 offers scalable and efficient image storage solutions for dynamic web applications.

---

## Scope 😲
- **Direct Image Uploads to AWS S3**: Store images directly in a cloud-based S3 bucket for better scalability and accessibility.
- **Simple Image Management**: Users can upload, display, and manage their images via a clean web interface.
- **Secure File Storage**: Leverage AWS's high-security infrastructure for storing images.
- **Anywhere, Anytime Access**: Users can upload images from any device with internet access and display them instantly on the website.
- **Ideal for Developers & Content Managers**: Perfect for web developers, digital marketers, and content creators who need easy image management solutions.

---

## Tech Stack 🛠️

<details>  
<summary>Frontend</summary>  
<ul>  
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML">HTML</a></li>  
  <li><a href="https://developer.mozilla.org/en-US/docs/Web/HTML">CSS</a></li>  
</ul>  
</details>

<details>  
<summary>Backend</summary>  
<ul>  
  <li><a href="https://www.djangoproject.com/">Django</a></li>  
  <li><a href="https://www.python.org/">Python</a></li>  
</ul>  
</details>

<details>  
<summary>Cloud & Storage</summary>  
<ul>  
  <li><a href="https://aws.amazon.com/s3/">Amazon S3</a></li>  
  <li><a href="https://boto3.amazonaws.com/v1/documentation/api/latest/index.html">Boto3 (AWS SDK for Python)</a></li>  
</ul>  
</details>

---

## Features ⚙️

### User Functions:
- **Upload Images**: Users can upload images from their local devices to an S3 bucket.
- **View Uploaded Images**: Display all uploaded images on the website with a gallery view.
- **Manage Images**: Users can view, delete, or update images they have uploaded.

### Admin Functions:
- **Image Management Dashboard**: Admin can manage the uploaded images, such as deleting or approving images.
- **Storage Analytics**: Monitor storage usage on AWS S3 directly from the backend.

---

## Requirements 📋
1. **Python 3.10+**: [Download](https://www.python.org/downloads/).
2. **Django 3.x+**: Install with `pip install django`.
3. **AWS Account**: Create an AWS account and set up an S3 bucket for storing images.
4. **AWS IAM User**: Set up an IAM user with AmazonS3FullAccess permissions and generate credentials for use with Boto3.

---

## Setup & Installation 🚀

```bash
# Clone the repository
git clone https://github.com/yourusername/SnapUp.git
cd SnapUp

# Create and activate a virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install required packages
pip install -r requirements.txt

# Set up AWS credentials (AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY)
# Add your S3 Bucket name to the Django settings file
# Follow AWS best practices for security

# Apply database migrations
python manage.py migrate

# Create a superuser to access the admin panel
python manage.py createsuperuser

# Run the development server
python manage.py runserver
```
## Usage 🎯
- **Upload Images**: Go to the image upload page, select an image file, and click "Upload".
- **View Images**: After uploading, you can view all the images uploaded in a gallery-style display.
- **Admin Panel**: Access the Django admin panel (`/admin`) to manage images and monitor uploads.

---

## Roadmap 🚀
- [ ] **User Authentication**: Add user authentication to allow users to view/upload images securely.
- [ ] **Image Resizing**: Automatically resize images during the upload to optimize storage and performance.
- [ ] **Image Tags & Categories**: Allow users to add tags or categories to images for better organization.
- [ ] **Advanced Image Editing**: Integrate tools for basic image editing (cropping, rotating) before uploading.
- [ ] **Mobile-Friendly UI**: Improve the interface for better responsiveness on mobile devices.

---

## Known Issues 🚧
- **Large Image Uploads**: Ensure images are within the limits of your AWS S3 bucket's storage quota.
- **Permissions**: If there are issues with image uploads, check the AWS IAM permissions and S3 bucket policy.

---

## Contributing 🤝
Pull requests are welcome! If you have any feature suggestions or bug fixes, feel free to open an issue or contribute directly to the project.

---

## Preview 👀
[SNAP UP PREVIEW](https://drive.google.com/file/d/1UUKbK3iA6nijW5rGb7DneflI4NKedBa7/view?usp=sharing)

---

## Acknowledgements 🎉
- Developed with guidance from **Mr. Tim Ruscica**.
- Special thanks to **AWS** for providing the cloud infrastructure.
- [Django Documentation](https://docs.djangoproject.com/en/stable/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)

---

## License 📄
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
