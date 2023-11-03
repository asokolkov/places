import { ReactNode } from 'react';

type PropsTypes = {
    icon: ReactNode;
};

function IconButton({icon}: PropsTypes) {
    return (
        <button className="w-[48px] h-[48px] rounded-global justify-center items-center">
            {icon}
        </button>
    );
}

export default IconButton;