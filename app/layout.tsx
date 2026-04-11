import type { Metadata } from 'next'
import Analytics from '@/components/Analytics'
import './globals.css'

export const metadata: Metadata = {
  title: 'PayrollPicker.com | Find the right payroll software in 60 seconds',
  description:
    'Answer 5 quick questions and get a personalized payroll software recommendation. Compare Gusto, OnPay, QuickBooks Payroll, Patriot, Rippling, and ADP — free, no email required.',
  openGraph: {
    title: 'PayrollPicker.com | Find the right payroll software in 60 seconds',
    description:
      'Answer 5 quick questions and get a personalized payroll software recommendation. Free, no email required.',
    url: 'https://payrollpicker.ai',
    siteName: 'PayrollPicker',
    type: 'website',
  },
  twitter: {
    card: 'summary_large_image',
    title: 'PayrollPicker.com | Find the right payroll software in 60 seconds',
    description:
      'Answer 5 quick questions and get a personalized payroll software recommendation.',
  },
  metadataBase: new URL('https://payrollpicker.ai'),
  alternates: {
    canonical: '/',
  },
}

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode
}>) {
  return (
    <html lang="en" className="scroll-smooth dark">
      <head>
        <link rel="preconnect" href="https://fonts.googleapis.com" />
        <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
        <link
          href="https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@300;400;500;700&family=Inter:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500;700&family=Instrument+Serif:ital@0;1&display=swap"
          rel="stylesheet"
        />
        <link
          href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:wght,FILL@100..700,0..1&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="font-sans bg-bg text-ink overflow-x-hidden">
        {children}
        <Analytics />
      </body>
    </html>
  )
}
