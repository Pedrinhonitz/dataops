def remove_diacritics(s):
    from unicodedata import normalize, category
    return ''.join(
        (c for c in normalize('NFD', s) if category(c) != 'Mn')
    )


def camel_case_to_snake_case(str):
    retstr = ''.join(
        ['_'+i.lower() if i.isupper() else i for i in str]
    ).lstrip('_')
    
    return retstr.replace('__', '_')


def transform(self, df, fields):
        from numpy import nan
        from pandas import to_datetime

        if df.empty:
            return df

        new_df = df.copy()

        for col in fields:
            col_val = fields[col]

            col_dest_name = None
            col_cast_type = None
            col_replace = None
            col_fn = None
            col_is_optional = False
            col_date_format = None
            col_fillna = None

            if isinstance(col_val, str):
                col_dest_name = col_val
            elif isinstance(col_val, dict):
                col_dest_name = col_val.get('rename', col)
                col_fn = col_val.get('fn')
                col_cast_type = col_val.get('type')
                col_replace = col_val.get('replace')
                col_is_optional = col_val.get('optional', False)
                col_date_format = col_val.get('date_format')
                col_fillna = col_val.get('fillna')
            else:
                raise Exception(f'Not able to parse fields for {col_val}, should be dict or str')

            if col_is_optional and (not col in new_df.columns):
                new_df[col] = nan

            try:
                if col_replace:
                    new_df[col] = new_df[col].replace(col_replace)

                if col_fn:
                    new_df[col] = new_df[col].apply(col_fn)

                if col_cast_type:
                    new_df[col] = new_df[col].astype(col_cast_type)
                
                if col_date_format:
                    new_df[col] = to_datetime(new_df[col], format=col_date_format)
                
                if col_fillna:
                    new_df[col] = new_df[col].fillna(col_fillna)

                if col_dest_name:
                    new_df = new_df.rename(columns={col: col_dest_name})

            except KeyError:
                new_df[col_dest_name] = None

        columns_not_avaiable = list(set(self.columns) - set(new_df.columns))
        new_df[columns_not_avaiable] = None

        return new_df[self.columns]