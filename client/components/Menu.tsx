import { useEffect, useState } from 'react';
import IconDiscover from 'icons/IconDiscover.tsx';
import IconProfile from 'icons/IconProfile.tsx';
import MenuButton from 'components/MenuButton.tsx';
import { useLocation, useNavigate } from 'react-router-dom';

type PropsTypes = {

};

function Menu({}: PropsTypes) {
    const location = useLocation();
    const currentPath = location.pathname;
    const [activeButtonId, setActiveButtonId] = useState(currentPath);
    const navigate = useNavigate();

    useEffect(() => {
        setActiveButtonId(currentPath);
    }, [currentPath]);

    function toggleButton(path: string) {
        if (path !== currentPath) {
            navigate(path);
        }
    }

    let buttons = {
        '/discover': {icon: <IconDiscover />, text: 'Просмотр'},
        '/profile': {icon: <IconProfile />, text: 'Профиль'},
    };

    return (
        <footer className="flex p-m rounded-t-global bg-white">
            {Object.entries(buttons).map(([path, {icon, text}]) => <MenuButton
                key={path}
                icon={icon}
                text={text}
                active={path === activeButtonId}
                onClick={() => toggleButton(path)}
            />)}
        </footer>
    );
}

export default Menu;