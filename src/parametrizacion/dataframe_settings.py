COLUMNS_MAPPING = {

    "tutelas" : {
        "NOMBRE DEL ACCIONANTE" : "nombreAccionante",
        "CEDULA" : "numDocumentoAccionante"
    },

    "solicitudes": {
        "RADICADO" : "radicado",
        "PROCESO" : "proceso",
        "NOMBRE_REMITENTE": "nombreAccionante",
        "DOCUMENTO_DE_REMITENTE": "numDocumentoAccionante",
        "TIPO_DE_DOCUMENTO_REMITENTE": "tipoDocumentoRemitente",
        "EMAIL_REMITENTE": "emailRemitente"
    },

    "consolidado": {
        "NOMBRE_DOCENTE" : "nombreAccionante",
        "CC DOCENTE" : "numDocumentoAccionante"
        
    },
    "solicitudes-2": {
        "NOMBRE_REMITENTE": "nombreAccionante",
        "DOCUMENTO_DE_REMITENTE": "numDocumentoAccionante",
        "TIPO_DE_DOCUMENTO_REMITENTE": "tipoDocumentoRemitente"
    },

}

EXPECTED_COLUMNS = ['radicado', 'proceso', 'nombreAccionante', 'numDocumentoAccionante', 'tipoDocumentoRemitente', 'emailRemitente']