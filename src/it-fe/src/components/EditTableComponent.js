import {useEffect, useState} from "react";
import axios from "axios";
import {backend_url} from "../const";
import {unstringifyValue} from "../utils";

export const ViewAndEditTableComponent = () => {
    const [database, setDatabase] = useState("")
    const [tableName, setTableName] = useState("")
    const [tableData, setTableData] = useState(null)
    const [editColumn, setEditColumn] = useState("")
    const [editValue, setEditValue] = useState(null)
    const [row, setRow] = useState(0)
    const [isOK, setIsOK] = useState(false)

    const handleGetTable = async (event) => {
        event.preventDefault()
        const response = await axios.get(
            `${backend_url}/database/${database}/table/${tableName}`
        )
        if (response.status < 400) {
            setTableData(response.data.result)
        }
    }
    const processValue = (value) => {
        if (value.low && value.high) {
            return `${value.low} - ${value.high}`
        }
        return value
    }


    const handleEditSubmit = async (event) => {
        event.preventDefault()
        const val = unstringifyValue(editValue)
        console.log(typeof val)
        console.log(val)
         const response = await axios.patch(
            `${backend_url}/database/${database}/table/${tableName}/edit_value`,
            {
                "row_id": Number(row),
                "value": val,
                "column_name": editColumn
            }
        )
        if (response.status < 400) {
            setIsOK(true)
        } else {
            setIsOK(false)
        }
    }
    return (
        <>
            <form onSubmit={handleGetTable}>
                <p> Database name </p>
                <input onChange={event => setDatabase(event.target.value)} />
                <p> Table name </p>
                <input onChange={event => setTableName(event.target.value)}/>
                <button> Get Table </button>
            </form>
            {
                tableData
                    ?
                    <>
                        <table style={{"borderWidth":"1px", 'borderColor':"#aaaaaa", 'borderStyle':'solid'}}>
                            <tbody>
                                {
                                    tableData.map((row, i) => {
                                        return (
                                            <tr key={i.toString()}>
                                                {
                                                    tableData[i].map(
                                                        value =>
                                                            <td key={i.toString() + value.toString()}  style={{"borderWidth":"1px", 'borderColor':"#aaaaaa", 'borderStyle':'solid'}}>
                                                                {`${processValue(value)}`}
                                                            </td>
                                                    )
                                                }
                                            </tr>
                                        )
                                    })
                                }
                            </tbody>
                        </table>
                        <form onSubmit={handleEditSubmit}>
                            <p> Column to edit </p>
                            <input onChange={event => setEditColumn(event.target.value)}/>
                            <p> Row to edit </p>
                            <input onChange={event => setRow(event.target.value)}/>
                            <p> New value </p>
                            <input onChange={event => setEditValue(event.target.value)}/>
                            <button> Edit value </button>
                        </form>
                        {isOK ? <b> OK, value edited! Press button again to show changes! </b> : <></>}
                    </>
                    :   <> </>
            }
        </>
    )
}