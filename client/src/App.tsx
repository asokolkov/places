import { Outlet } from 'react-router-dom';
import Header from 'components/Header.tsx';
import Menu from 'components/Menu.tsx';

function App() {
    return (
        <>
            <Header />
            <Outlet />
            <Menu />
        </>
    );
}

export default App;
