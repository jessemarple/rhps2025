# The Rocky Horror Picture Show - 25th Anniversary Website

A stunning, modern website for a community theater's 25th anniversary production of The Rocky Horror Picture Show, celebrating both the theater's milestone and the film's 50th anniversary.

## 🎭 Features

- **Beautiful Design**: Rocky Horror themed with red, purple, pink, and gold color scheme
- **Responsive Layout**: Works perfectly on desktop, tablet, and mobile devices
- **Ticket Sales**: Dedicated ticket purchasing page with show selection
- **Interactive Elements**: Hover effects, animations, and modern UI components
- **Contact Information**: Complete contact page with form and FAQ section
- **About Section**: Information about the production and theater history

## 📅 Show Information

- **Dates**: October 24th & 25th, 2025
- **Times**: 8:00 PM & 11:59 PM each night
- **Pricing**:
  - Online: $25 (Prop kit included)
  - At Door: $25 (Prop kit $5 if available)

## 🚀 Getting Started

### Prerequisites

- Node.js (version 18 or higher)
- npm or yarn

### Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd RHPS2025
```

2. Install dependencies:

```bash
npm install
```

3. Start the development server:

```bash
npm run dev
```

4. Open your browser and navigate to `http://localhost:4321`

### Building for Production

```bash
npm run build
```

The built files will be in the `dist/` directory.

## 🛠️ Technology Stack

- **Astro**: Modern static site generator
- **Tailwind CSS**: Utility-first CSS framework
- **TypeScript**: Type-safe JavaScript
- **Google Fonts**: Playfair Display & Roboto for typography

## 📁 Project Structure

```
src/
├── components/
│   └── Navigation.astro      # Site navigation component
├── layouts/
│   └── Layout.astro          # Main layout with styling
├── pages/
│   ├── index.astro           # Homepage
│   ├── tickets.astro         # Ticket purchasing page
│   ├── about.astro           # About the production
│   └── contact.astro         # Contact information and form
└── styles/
    └── global.css            # Global Tailwind styles
```

## 🎨 Customization

### Colors

The site uses custom CSS variables for the Rocky Horror theme:

- `--rhps-red`: #dc2626
- `--rhps-purple`: #7c3aed
- `--rhps-pink`: #ec4899
- `--rhps-gold`: #f59e0b

### Fonts

- **Playfair Display**: Used for headings and titles
- **Roboto**: Used for body text and navigation

## 📧 Contact Information

Update the contact information in `src/pages/contact.astro` with your actual:

- Email address
- Phone number
- Theater address
- Box office hours

## 🎫 Ticket Integration

The ticket purchasing system is currently set up with a form interface. To integrate with a real payment processor:

1. Add your payment gateway (Stripe, PayPal, etc.)
2. Update the form action in `src/pages/tickets.astro`
3. Add server-side processing for ticket validation
4. Implement email confirmation system

## 🚀 Deployment

### Netlify

1. Connect your repository to Netlify
2. Set build command: `npm run build`
3. Set publish directory: `dist`

### Vercel

1. Connect your repository to Vercel
2. Vercel will automatically detect Astro and deploy

### Other Platforms

The site can be deployed to any static hosting platform since it's built with Astro.

## 📝 License

This project is created for educational and commercial use. Please ensure you have the necessary rights to use Rocky Horror Picture Show branding and content.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## 🎭 About Rocky Horror

The Rocky Horror Picture Show is a 1975 musical comedy horror film that has become a cult classic. The film's interactive nature, where audiences participate with props and callbacks, has made it a unique theatrical experience that continues to captivate audiences worldwide.

---

_"Don't dream it, be it!" - Dr. Frank-N-Furter_
