import {useState} from "react";
import axios from "axios";
import {backend_url} from "../const";

export const CreateDBComponent = () => {
    const [dbName, setDbName] = useState("")
    const [isOK, setIsOK] = useState(false)
    const inputHandler = (event) => {
        setDbName(event.target.value)
    }
    const formHandler = async (event) => {
        event.preventDefault()
        const response = await axios.post(
            `${backend_url}/database/create`,
            {
                "database_name": dbName
            })
        console.log(response)
        if (response.status < 400) {
            setIsOK(true)
        }
    }
    return (
        <>
            <form onSubmit={formHandler}>
                <input onChange={inputHandler} />
                <button> Sumbit! </button>
            </form>
            {isOK ? <b> OK, database created! </b> : <></>}
        </>
    )
}