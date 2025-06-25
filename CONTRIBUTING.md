# Contributing to Buildables

Thank you for your interest in contributing to the Buildables project! We welcome all contributions, especially those that enhance the frontend experience for our community.

## How to Contribute

1. **Fork the Repository**
   - Click the "Fork" button at the top right of this repository page to create your own copy.

2. **Clone Your Fork**
   - Clone your forked repository to your local machine:
     ```sh
     git clone https://github.com/your-username/Buildables.git
     cd Buildables
     ```

3. **Create a New Branch**
   - Create a branch for your feature or bugfix:
     ```sh
     git checkout -b feature/your-feature-name
     ```

4. **Make Your Changes**
   - Most frontend files are in the `website/` directory:
     - HTML: `website/*.html`
     - CSS: `website/css/styles.css`
     - JavaScript: `website/js/`
   - Please follow the existing code style and structure.

5. **Test Your Changes**
   - Run the frontend locally to ensure your changes work as expected:
     ```sh
     cd website
     python -m http.server 8000
     # Visit http://localhost:8000 in your browser
     ```

6. **Commit and Push**
   - Commit your changes with a clear message:
     ```sh
     git add .
     git commit -m "Describe your enhancement or fix"
     git push origin feature/your-feature-name
     ```

7. **Open a Pull Request**
   - Go to your fork on GitHub and click "Compare & pull request".
   - Fill in the PR template and describe your changes.

## Guidelines

- Focus on frontend enhancements (UI/UX, accessibility, interactivity, etc.).
- Keep pull requests focused and concise.
- Write clear, descriptive commit messages.
- Test your changes before submitting.
- Be respectful and constructive in code reviews and discussions.

## Need Help?

If you have questions or need help, open an issue or start a discussion in the repository.

Happy contributing!

— The Buildables Team
