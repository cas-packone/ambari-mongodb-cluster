mongo --port $1 << EOF
use admin;
db.shutdownServer();
EOF
