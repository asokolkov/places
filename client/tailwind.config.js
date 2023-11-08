/** @type {import('tailwindcss').Config} */
export default {
    content: ['./src/**/*.{html,js,svelte,ts}'],
    theme: {
        extend: {
            colors: {
                'background': '#F3F3F3',
                'primary': '#C2EB2D',
                'black': '#1E1E1E',
                'white': '#FFF',
                'inactive': '#858585',
                'error': '#E24848',
            },
            fontSize: {
                'h1': ['24px', {
                    lineHeight: '32px',
                    fontWeight: '600',
                }],
                'h2': ['20px', {
                    lineHeight: '24px',
                    fontWeight: '500',
                }],
                'h3': ['16px', {
                    lineHeight: '16px',
                    fontWeight: '600',
                }],
                'p': ['15px', {
                    lineHeight: '16px',
                    fontWeight: '500',
                }],
            },
            spacing: {
                s: '8px',
                m: '16px',
                l: '24px',
                element: '48px'
            },
            borderRadius: {
                'global': '16px',
            },
            flex: {
                'fill': '1 0 0',
            },
            boxShadow: {
                'element': '0 0 12px 2px rgba(0, 0, 0, 0.06)',
            },
        },
    },
    plugins: [],
}

