import { Outlet } from 'react-router-dom';
import Header from 'components/Header.tsx';
import Menu from 'components/Menu.tsx';

function App() {
    return (
        <div className="flex flex-col h-full">
            <Header />
            <Outlet />
            <Menu />
        </div>
    );
}

export default App;
