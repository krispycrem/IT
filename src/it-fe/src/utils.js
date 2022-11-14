function isInt(n){
    return !(Number.isNaN(Number.parseInt(n)));
}

function isFloat(n){
    return !(Number.isNaN(Number.parseFloat(n)));
}

function isRange(str){
    return str.includes("low")
}

export function unstringifyValue(val) {
    let new_val = val
    if (isInt(val) || isFloat(val)) {
        new_val = Number(val)
    }
    else if (isRange(val)) {
        new_val = JSON.parse(val)
    }
    return new_val
}