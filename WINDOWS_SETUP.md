# Windows Setup Instructions for AI Voice Surrogate Project

This document provides step-by-step instructions for setting up and running the PhoneAgent project on a Windows computer.

## Prerequisites
Ensure you have the following installed on your Windows machine:
- **Python 3.10+**: Download the installer from [python.org](https://www.python.org/downloads/). **Important:** During installation, ensure you check the box that says "Add Python 3.x to PATH".
- **Node.js & npm 18+**: Download the Windows Installer (.msi) from [nodejs.org](https://nodejs.org/).
- **MongoDB**: Download and install the [MongoDB Community Server](https://www.mongodb.com/try/download/community). It's recommended to install it as a service so it runs automatically on port 27017. You may also want to install MongoDB Compass for a graphical interface.
- **Ngrok**: Download the Windows zip file from [ngrok.com](https://ngrok.com/download), extract the executable, and ideally add the folder containing `ngrok.exe` to your system's PATH environment variable. Alternatively, if you use Chocolatey, run `choco install ngrok`.

---

## Step 1: Environment Variables
Create a `.env` file in the **root** of the `PhoneAgent` directory with the following API Keys:

```env
MONGO_URI=mongodb://localhost:27017
ELEVENLABS_API_KEY=your_elevenlabs_key
GEMINI_API_KEY=your_gemini_key
TWILIO_ACCOUNT_SID=your_twilio_sid
TWILIO_AUTH_TOKEN=your_twilio_auth_token
TWILIO_PHONE_NUMBER=+1234567890
```

*Note: Your `TWILIO_PHONE_NUMBER` must be exactly formatted with the `+` sign and country code, and MUST be an active/verified number you own.*

---

## Step 2: Running the Python Backend
The Python backend uses FastAPI to expose Webhooks and handle the WebSockets logic securely.

1. Open Command Prompt or PowerShell and navigate to the root `PhoneAgent` directory.
2. Navigate to the backend folder, initialize, and activate a virtual environment:
   ```cmd
   cd backend
   python -m venv venv
   venv\Scripts\activate
   ```
3. Install dependencies:
   ```cmd
   pip install -r requirements.txt
   ```
4. Start the Uvicorn server (run this from the root `PhoneAgent` directory):
   ```cmd
   cd ..
   uvicorn backend.main:app --host 0.0.0.0 --port 8000
   ```

---

## Step 3: Running the React Frontend
The Dashboard uses Next.js 16 (App Router) with Tailwind CSS.

1. Open a **new** Command Prompt or PowerShell window and navigate to the frontend directory:
   ```cmd
   cd PhoneAgent\frontend
   ```
2. Install npm packages:
   ```cmd
   npm install
   ```
3. Run the development server:
   ```cmd
   npm run dev
   ```
4. View the frontend at [http://localhost:3000](http://localhost:3000)

---

## Step 4: Exposing the Webhook via Ngrok
Because Twilio requires a public URL to send Webhooks to, we must proxy our `8000` port to the internet.

1. Open a **third** Command Prompt or PowerShell window.
2. Ensure you have authenticated Ngrok:
   ```cmd
   ngrok config add-authtoken YOUR_TOKEN
   ```
3. Run the HTTP tunnel pointing to our backend port:
   ```cmd
   ngrok http 8000
   ```
   *(If you didn't add ngrok to your PATH, you will need to provide the full path to `ngrok.exe` or run this command from the directory where `ngrok.exe` is located).*

---

## Step 5: Configuring Twilio
1. Once Ngrok starts, copy the Forwarding URL (e.g., `https://something.ngrok-free.dev`).
2. Log into the Twilio Developer Console.
3. Find your active Phone Number > "Voice & Fax" settings.
4. Set "A CALL COMES IN" to a Webhook URL that looks precisely like: `https://[YOUR_NGROK_URL]/twiml` using POST.
5. Save the configuration.

You can now test outbound dialing through the UI at `localhost:3000` or dial the Twilio number directly to initiate the system inbound!
