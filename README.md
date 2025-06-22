# 🧠 CV to Portfolio Site Converter

This project is a simple yet powerful tool that transforms a user's CV (in PDF format) into a personalized portfolio website using a language model. It enables rapid prototyping of developer portfolios by leveraging structured data extraction and a TypeScript React frontend.

## ✨ Features

- 🔄 **Convert CV PDF to structured JSON**
- 🤖 **LLM-assisted parsing via HuggingFace**
- 🧩 **Editable output JSON (`info.json`) for customization**
- 🌐 **TypeScript/TSX website template that renders the portfolio**
- 🔧 **User-friendly configuration and deployment**

---

## 🛠 How It Works

1. **Upload a CV PDF**  
   The user uploads a PDF version of their CV to the system.

2. **LLM Parsing**  
   The backend submits the PDF to a language model hosted on HuggingFace, using a HuggingFace Access Token (provided by the user via a `.env` file in the ai_extraction folder).

3. **Generate JSON**  
   The response from the LLM is structured into a predefined JSON format, representing the user’s professional profile.

4. **Render Portfolio**  
   A pre-built TSX website uses this `info.json` to populate and render a personalized portfolio.

5. **Edit and Customize**  
   Users can manually refine or extend their `info.json` file for more control over the final site.

---

## 📁 JSON Output Format

The generated `info.json` file follows this structure:

```json
{
  "name": "John Doe",
  "current_workplace": "OpenAI",
  "bio": "Passionate ML researcher...",
  "relevant_experience_history": [
    {
      "company": "OpenAI",
      "role": "Research Engineer",
      "start_date": "2020-01",
      "end_date": "Present",
      "experiences": "Worked on GPT and multimodal models..."
    }
  ],
  "coding_projects": [
    {
      "project_name": "SmartVision",
      "technologies": ["Python", "TensorFlow"],
      "description": "A deep learning project for object detection.",
      "demoLink": "https://demo.example.com",
      "githubLink": "https://github.com/johndoe/smartvision"
    }
  ],
  "contact": {
    "email": "john@example.com",
    "linkedIn": "https://linkedin.com/in/johndoe",
    "github": "https://github.com/johndoe"
  },
  "other": []
}
```

---

## 🔐 Environment Configuration

Before starting, create a `.env` file at the root of your project with your [HuggingFace Access Token](https://huggingface.co/docs/hub/security-tokens):

```bash
token=your_token_here
```

---

## 🚀 Getting Started

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/cv-to-portfolio.git
   cd cv-to-portfolio
   ```

2. **Install dependencies**
   ```bash
   npm install
   ```

3. **Set your HuggingFace token (Need to signup to huggingface)**
   ```bash
   echo "token=your_token" > cvAnalyzer/ai_extraction/.env
   ```
   
4. **Put CV into resources folder**

5. **Run the cvAnalyzer**
    run the python main file
   ```bash
   python cvAnalyzer/main.py 
   ```
  
6. **Run the portfolio site**
   ```bash
   cd siteCreator/site
   npm start
   ```
   
7. **Edit data.json file to your liking**

---

## 🎨 Customization

- Manually edit `info.json` to fine-tune the site’s content
- You can add new fields, sections, or modify layout/styling in the TSX components
- Extend support for other model providers if desired (e.g., OpenAI API)

---

## 🧩 Tech Stack

- **Frontend**: React + TypeScript (TSX)
- **Backend/Parsing**: LLM API via HuggingFace
- **PDF Parsing**: pdf-parse or similar
- **Deployment**: In progress

---

## 📄 License

MIT License — feel free to use and adapt!

---

## 🤝 Contributing

If you'd like to contribute, discuss improvements, or add support for more output formats (like Markdown resumes or LaTeX CVs), feel free to open an issue or submit a PR.

---

