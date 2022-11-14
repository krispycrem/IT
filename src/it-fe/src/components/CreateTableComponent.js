import {useState} from "react";
import axios from "axios";
import {backend_url} from "../const";
import _ from "lodash"

export const CreateTableComponent = () => {
    const [dbName, setDbName] = useState("")
    const [tableName, setTableName] = useState("")
    const [columns, setColumns] = useState([{column:"", type:""}])
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
            `${backend_url}/database/${dbName}/table/create`,
            {
                "table_name": tableName,
                "columns": columns.reduce(
                    (obj, currentColumn) => {
                        console.log(obj)
                        obj[currentColumn["column"]] = currentColumn["type"]
                        return obj
                    }, {}
                )
            })
        console.log(response)
        if (response.status < 400) {
            setIsOK(true)
        }
    }
    const handleNewColumn = (event) => {
        let newColumn = { column: '', type: '' }
        setColumns(columns.concat(newColumn))
    }
    const handleColumnData = (event, index) => {
        const {name, value} = event.target
        const clone = _.cloneDeep(columns)
        clone[index][name] = value
        setColumns(clone)
    }
    return (
        <>
            <button onClick={handleNewColumn}> Add new column </button>
            <form onSubmit={formHandler}>
                <p> Database name </p>
                <input onChange={inputDatabaseHandler} />
                <p> Table name </p>
                <input onChange={inputTableHandler} />
                <p> Columns </p>
                {
                    columns.map((input, i) => {
                        return (
                            <div key={i}>
                                <input name={"column"} value={input.column} onChange={event => handleColumnData(event, i)}/>
                                <input name={"type"} value={input.type} onChange={event => handleColumnData(event, i)}/>
                            </div>
                        )
                        }
                    )
                }
                <button> Sumbit! </button>
            </form>
            {isOK ? <b> OK, table created! </b> : <></>}
        </>
    )
}