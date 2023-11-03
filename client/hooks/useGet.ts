import { useEffect, useState } from 'react';
import axios from 'axios';

function useGet(url: string) {
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        axios.get(url)
            .then(res => {
                setResponse(res.data);
                setError(null);
            })
            .catch(res => {
                setResponse(null);
                setError(res);
            })
            .finally(() => {
                setLoading(false);
            });
    }, []);

    return {response, loading, error};
}

export default useGet;