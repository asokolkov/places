import { ReactNode } from 'react';
import { useNavigate } from 'react-router-dom';

type PropsTypes = {
    icon: ReactNode;
    text: string;
    active: boolean;
    path: string;
    onClick: () => void;
};

function MenuButton({icon, text, active, path, onClick} : PropsTypes) {
    function handleClick() {
        onClick();
        navigate(path);
    }
    
    const navigate = useNavigate();
    let color = active ? 'text-white' : 'text-black';
    let bgColor = active ? 'bg-black' : 'bg-white';

    return (
        <button onClick={handleClick} className={`flex h-[48px] w-full rounded-block gap-s flex-row justify-center items-center ${color} ${bgColor}`}>
            {icon}
            {active && text}
        </button>
    );
}

export default MenuButton;