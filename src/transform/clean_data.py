def clean_quartieri(quartieri):
    quartieri = quartieri.copy()

    quartieri["quartiere_name_clean"] = (
        quartieri["DENOM"]
        .astype(str)
        .str.lower()
        .str.strip()
    )

    return quartieri