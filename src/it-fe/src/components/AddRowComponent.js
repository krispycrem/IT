import {useState} from "react";
import axios from "axios";
import {backend_url} from "../const";

export const AddRowComponent = () => {
    const [rowData, setRowData] = useState("")
    const [dbName, setDbName] = useState("")
    const [tableName, setTableName] = useState("")
    const [isOK, setIsOK] = useState(false)

    const inputDatabaseHandler = (event) => {
        setDbName(event.target.value)
    }
    const inputTableHandler = (event) => {
        setTableName(event.target.value)
    }
    const rowDataHandler = (event) => {
        setRowData(event.target.value)
    }

    const formHandler = async (event) => {
        event.preventDefault()
        const bodyFormData = new FormData();
        bodyFormData.append('row_data', rowData)
        const response = await axios.post(
            `${backend_url}/database/${dbName}/table/${tableName}/add_row`,
            bodyFormData,
            { headers: {"Content-Type": "multipart/form-data" }})
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
                <p> Row data (in JSON format) </p>
                <textarea onChange={rowDataHandler} />
                <button> Sumbit! </button>
            </form>
            {isOK ? <b> OK, row added! </b> : <></>}
        </>
    )
}