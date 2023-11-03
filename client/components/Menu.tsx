import { useState } from 'react';
import IconDiscover from 'icons/IconDiscover.tsx';
import IconProfile from 'icons/IconProfile.tsx';
import MenuButton from 'components/MenuButton.tsx';

type PropsTypes = {

};

function Menu({}: PropsTypes) {
    const [activeButton, setActiveButton] = useState(0);

    function toggleButton(id: number) {
        setActiveButton(id);
    }

    let buttons = [
        {id: 0, icon: <IconDiscover />, text: 'Просмотр', path: '/discover'},
        {id: 1, icon: <IconProfile />, text: 'Профиль', path: '/profile'},
    ];

    return (
        <footer className="flex fixed right-0 bottom-0 left-0 p-m rounded-t-global bg-white">
            {buttons.map(({id, icon, text, path}) => <MenuButton
                key={id}
                icon={icon}
                text={text}
                active={id === activeButton}
                path={path}
                onClick={() => toggleButton(id)}
            />)}
        </footer>
    );
}

export default Menu;