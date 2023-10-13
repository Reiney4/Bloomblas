import axios from '../utils/api';

export const loginRequest = async ({ email, password }) => {
    await axios.post('/users/login', { email, password })
    .then((response) => {
        if (response.status === 200) {
            return response.data;
        }
    }).catch((error) => {
        // Handle error.
        console.log(error);
    });
}