import useGet from 'hooks/useGet.ts';
import { useNavigate } from 'react-router-dom';
import { useEffect, useState } from 'react';

type PropsTypes = {
    
};

function DiscoverPage({}: PropsTypes) {
    const {response, loading, error} = useGet('https://jsonplaceholder.typicode.com/todos');
    const navigate = useNavigate();
    const [data, setData] = useState([]);

    useEffect(() =>{
        if (error !== null) {
            navigate('/error');
        }
        if (response && !loading) {
            setData(response);
        }
    }, [response, loading, error]);

    return (
        <div className="flex self-stretch flex-fill flex-col overflow-y-scroll">
            {loading ? 'Пока пусто' : data.map(x => <p>{x.title}</p>)}
        </div>
    );
}

export default DiscoverPage;