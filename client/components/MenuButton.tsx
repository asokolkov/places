import { ReactNode } from 'react';

type PropsTypes = {
    icon: ReactNode;
    text: string;
    active: boolean;
    onClick: () => void;
};

function MenuButton({icon, text, active, onClick} : PropsTypes) {
    let color = active ? 'text-white' : 'text-black';
    let bgColor = active ? 'bg-black' : 'bg-white';

    return (
        <button onClick={onClick} className={`flex h-[48px] w-full rounded-block gap-s flex-row justify-center items-center ${color} ${bgColor}`}>
            {icon}
            {active && text}
        </button>
    );
}

export default MenuButton;