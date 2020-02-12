# To get started with firebase 🔥

this script implements 💻
https://firebase.google.com/docs/projects/api/reference/rest/v1beta1/projects.webApps/getConfig

pipenv install

or alternatively
python3 -m venv <path/to/venv>
pip -r install requirements.txt

create service account within GCP and save as service-account.json
enable roles 💁
Firebase Admin
Firebase Authentication Admin

    EXAMPLE:

    gcloud iam service-accounts create [SA-NAME] \
    --description "[SA-DESCRIPTION]" \
    --display-name "[SA-DISPLAY-NAME]"

    gcloud projects add-iam-policy-binding my-project-123 \
    --member serviceAccount:my-sa-123@my-project-123.iam.gserviceaccount.com \
    --role roles/firebase.admin roles/firebaseauth.admin

## Finally run:

./generate-firebase-config.sh
