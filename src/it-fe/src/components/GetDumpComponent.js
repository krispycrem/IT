import {useState} from "react";
import axios from "axios";
import {backend_url} from "../const";

export const GetDumpComponent = () => {
    const [dbName, setDbName] = useState("")
    const [dump, setDump] = useState("")
    const [isOK, setIsOK] = useState(false)
    const inputDatabaseHandler = (event) => {
        setDbName(event.target.value)
    }
    const formHandler = async (event) => {
        event.preventDefault()
        const response = await axios.get(
            `${backend_url}/database/${dbName}/get_dump`,
        )
        console.log(response)
        if (response.status < 400) {
            setIsOK(true)
            setDump(response.data)
        }
    }
    return (
        <>
            <form onSubmit={formHandler}>
                <p> Database name </p>
                <input onChange={inputDatabaseHandler} />
                <button> Get dump! </button>
            </form>
            {isOK
                ?
                <>
                    <b> OK, got dump! </b>
                    <p>
                        {dump}
                    </p>
                </>
                : <></>}
        </>
    )
}