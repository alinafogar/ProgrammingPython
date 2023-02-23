    for i in range(1,12):
        if first_year[i]=='':
            variation.append('')

        var=first_year[i]-first_year[i-1]
        variation.append(var)