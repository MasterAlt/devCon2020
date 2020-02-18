FROM golang:1.12.1-alpine3.9
ENV GOPATH="/go"
RUN ["mkdir", "-p", "/go/src/github.com/rancher/demo"]
COPY * /go/src/github.com/rancher/demo/
WORKDIR /go/src/github.com/rancher/demo
#RUN apk update
#RUN apk add nodejs nodejs-npm
#RUN npm install sonarqube-scanner -g
RUN ["go", "build", "-o", "demo"]
CMD ["./demo"]
