
echo "Enter github Org"
read org

curl -i https://api.github.com/orgs/"$org"/repos | grep 'html_url' | sort | uniq | awk '{print $2}' | sed 's/\"//g' | sed 's/,//g' > $org'_repos.txt'

cat $org'_repos.txt'

echo "Searching creds...."

trufflehog $org'_repos.txt'