import { useLocation, useNavigate } from 'react-router-dom';
import MenuButton from 'components/MenuButton.tsx';
import IconDiscover from 'icons/IconDiscover.tsx';
import IconProfile from 'icons/IconProfile.tsx';
import { useEffect, useState } from 'react';

type PropsTypes = {

};

function Menu({}: PropsTypes) {
    const location = useLocation();
    const navigate = useNavigate();
    const [currentRoute, setCurrentRoute] = useState(location.pathname);

    useEffect(() => {
        setCurrentRoute(location.pathname);
    }, [location.pathname]);

    function onClick(route: string) {
        if (currentRoute !== route) {
            navigate(route);
        }
    }

    return (
        <footer className="flex p-m rounded-t-global bg-white">
            <MenuButton
                icon={<IconDiscover />}
                text="Просмотр"
                active={currentRoute === '/discover'}
                onClick={() => onClick('/discover')}
            />
            <MenuButton
                icon={<IconProfile />}
                text="Профиль"
                active={currentRoute === '/profile'}
                onClick={() => onClick('/profile')}
            />
        </footer>
    );
}

export default Menu;