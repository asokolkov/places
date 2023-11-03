import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.tsx'
import './index.css'
import { BrowserRouter, Navigate, Route, Routes } from 'react-router-dom';
import DiscoverPage from '../pages/DiscoverPage.tsx';
import ProfilePage from '../pages/ProfilePage.tsx';
import ErrorPage from 'pages/ErrorPage.tsx';

ReactDOM.createRoot(document.getElementById('root')!).render(
    <React.StrictMode>
        <BrowserRouter>
            <Routes>
                <Route element={<App />}>
                    <Route path="/" element={<Navigate to="/discover" />} />
                    <Route path="/discover" element={<DiscoverPage />} />
                    <Route path="/profile" element={<ProfilePage />} />
                    <Route path="/error" element={<ErrorPage />} />
                </Route>
            </Routes>
        </BrowserRouter>
    </React.StrictMode>,
);
