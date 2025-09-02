# PureArchitecture Automated Forms Messenger

# PureArchitecture Automated Forms Messenger

A highly scalable and enterprise-grade automation platform designed to seamlessly process Google Forms responses via Google Sheets, with integrated support for messaging channels such as WhatsApp and secure local data storage.

Developed for Pure Arquitetura, this solution ensures real-time notification of every form submission through WhatsApp or email, eliminating manual monitoring and significantly reducing response times. By automating the capture, processing, and summarization of customer inquiries, the system empowers the business to maximize sales opportunities and maintain exceptional client engagement. 

Built with a modular and extensible architecture, this platform enables rapid adaptation to evolving business needs, robust data handling, and effortless integration with additional communication or analytics tools. The result is a reliable, maintainable, and future-proof automation feature that delivers measurable operational efficiency and strategic value for high-performance teams.

---

## 🚀 Features

- **Google Sheets Integration:** Securely fetch and process form responses.
- **Messaging Automation:** Easily send notifications via WhatsApp or email.
- **Modular Architecture:** Clean separation of concerns for scalability and maintainability.
- **Environment Configuration:** Sensitive data managed via `.env` and `credentials.json`.
- **Extensible:** Ready for integration with other platforms or custom workflows.

---

## 📦 Project Structure

```
PureArchitecture_Automated_Forms_Messenger/
│
├── src/
│   ├── main.py
│   ├── google_sheets.py
│   ├── messenger.py
│   ├── email_sender.py
│   └── utils.py
├── requirements.txt
├── .env
├── credentials.json
├── .gitignore
└── README.md
```

---

## 🛠️ Setup & Usage

1. **Clone the repository**
   ```sh
   git clone https://github.com/seu-usuario/PureArchitecture_Automated_Forms_Messenger.git
   cd PureArchitecture_Automated_Forms_Messenger
   ```

2. **Install dependencies**
   ```sh
   pip install -r requirements.txt
   ```

3. **Configure credentials**
   - Place your Google API `credentials.json` in the project root.
   - Create a `.env` file with your environment variables (see example below).

4. **Run the application**
   ```sh
   python src/main.py
   ```

---

## 📝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

---

## 📄 License

This project is licensed under the MIT License.

---

## ✨ Author

Developed by [Guilherme Oleano](https://github.com/OleanoGui) — passionate about clean architecture and automation.
