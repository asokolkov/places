import MenuButton from 'components/MenuButton.tsx';
import IconDiscover from 'icons/IconDiscover.tsx';
import IconProfile from 'icons/IconProfile.tsx';
import { useState } from 'react';

function Menu() {
    const [activeButton, setActiveButton] = useState(0);

    function toggleButton(id: number) {
        setActiveButton(id);
    }

    let buttons = [
        {id: 0, icon: <IconDiscover />, text: 'Просмотр'},
        {id: 1, icon: <IconProfile />, text: 'Профиль'},
    ];

    return (
        <footer className="flex fixed right-0 bottom-0 left-0 p-m rounded-global bg-white">
            {buttons.map(({id, icon, text}) =>
                <MenuButton key={id} icon={icon} text={text} active={id === activeButton} onClick={() => toggleButton(id)} />
            )}
        </footer>
    );
}

export default Menu;