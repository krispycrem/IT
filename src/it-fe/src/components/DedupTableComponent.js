import {useState} from "react";
import axios from "axios";
import {backend_url} from "../const";

export const DedupTableComponent = () => {
    const [dbName, setDbName] = useState("")
    const [tableName, setTableName] = useState("")
    const [isOK, setIsOK] = useState(false)
    const inputDatabaseHandler = (event) => {
        setDbName(event.target.value)
    }
    const inputTableHandler = (event) => {
        setTableName(event.target.value)
    }
    const formHandler = async (event) => {
        event.preventDefault()
        const response = await axios.post(
            `${backend_url}/database/${dbName}/table/${tableName}/dedup`,
            )
        console.log(response)
        if (response.status < 400) {
            setIsOK(true)
        }
    }
    return (
        <>
            <form onSubmit={formHandler}>
                <p> Database name </p>
                <input onChange={inputDatabaseHandler} />
                <p> Table name </p>
                <input onChange={inputTableHandler} />
                <button> Dedup! </button>
            </form>
            {isOK ? <b> OK, dedup successful! </b> : <></>}
        </>
    )
}