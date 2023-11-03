import { useLocation } from 'react-router-dom';
import { useEffect, useState } from 'react';

type PropsTypes = {

};

function Header({}: PropsTypes) {
    const location = useLocation();
    const [currentRoute, setCurrentRoute] = useState(location.pathname);

    useEffect(() => {
        setCurrentRoute(location.pathname);
    }, [location.pathname]);

    const headers = {
        '/discover': 'Плейслисты',
        '/profile': 'Профиль',
    };

    return (
        <header className="flex h-[48px] bg-background">
            <h3 className="text-inactive m-auto">{headers[currentRoute]}</h3>
        </header>
    );
}

export default Header;