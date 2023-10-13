import axios from "axios";

const apiInstance = axios.create({
    baseURL: "http://127.0.0.1:5555",
    withCredentials : false,
    headers: {
        "Content-Type": "application/json",
        "Access-Control-Allow-Headers": true,
        "Access-Control-Allow-Origin": "*"
    }
});

export default apiInstance;