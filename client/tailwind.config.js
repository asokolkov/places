/** @type {import('tailwindcss').Config} */
export default {
    content: [
        './index.html',
        './src/**/*.{js,ts,jsx,tsx}',
        './components/**/*.{js,ts,jsx,tsx}',
        './pages/**/*.{js,ts,jsx,tsx}',
    ],
    theme: {
        extend: {
            colors: {
                'background': '#F3F3F3',
                'primary': '#C2EB2D',
                'black': '#1E1E1E',
                'white': '#FFF',
                'inactive': '#858585',
            },
            fontSize: {
                'p': ['15px', {
                    lineHeight: '16px',
                    fontWeight: '500',
                }],
                'h1': ['24px', {
                    lineHeight: '32px',
                    fontWeight: '600',
                }],
                'h2': ['20px', {
                    lineHeight: '24px',
                    fontWeight: '500',
                }],
            },
            spacing: {
                s: '8px',
                m: '16px',
                l: '24px',
            },
            borderRadius: {
                'global': '16px',
                'block': '8px',
            },
            flex: {
                'fill': '1 0 0',
            }
        },
    },
    plugins: [],
}

