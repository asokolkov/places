type PropsTypes = {

};

function Header({}: PropsTypes) {
    return (
        <header className="flex h-[48px] fixed top-0 right-0 left-0 bg-background">
            <h3 className="text-inactive m-auto">Плейслисты</h3>
        </header>
    );
}

export default Header;