
import type { Config } from "tailwindcss";

export default {
  darkMode: ["class"],
  content: [
    "./pages/**/*.{ts,tsx}",
    "./components/**/*.{ts,tsx}",
    "./app/**/*.{ts,tsx}",
    "./src/**/*.{ts,tsx}",
  ],
  prefix: "",
  theme: {
    extend: {
      colors: {
        background: "var(--background)",
        foreground: "var(--foreground)",
        "secondary-bg": "var(--secondary-bg)",
        muted: "var(--muted)",
        "muted-foreground": "var(--muted-foreground)",
        chat: {
          user: "var(--chat-user)",
          assistant: "var(--chat-assistant)"
        },
        accent: {
          DEFAULT: "var(--accent)",
          foreground: "var(--accent-foreground)"
        },
        success: "var(--success)",
      },
      maxWidth: {
        'chat': '800px',
      },
      fontFamily: {
        sans: [
          "-apple-system",
          "BlinkMacSystemFont",
          "San Francisco",
          "Helvetica Neue",
          "sans-serif"
        ],
      },
    },
  },
  plugins: [require("tailwindcss-animate")],
} satisfies Config;
