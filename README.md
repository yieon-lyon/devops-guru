# AWS DevOps Guru 시작하기

### AWS DevOps Guru를 활성화하여 잠재적인 운영 문제가 더 큰 문제로 커지기 전에 이를 알려줄 수 있는 환경을 조성하여 데이터베이스 모니터링을 더욱 견고히 한다.
![](https://velog.velcdn.com/images/yieon/post/cf63c070-52c3-4cb2-a60c-b7879e2fcccf/image.png)

#### Step1. AWS DevOps Guru 활성화

![](https://velog.velcdn.com/images/yieon/post/ef0fad6b-ddb8-40fc-b8a5-780ad95894eb/image.png)

![](https://velog.velcdn.com/images/yieon/post/a3c72de2-48c0-4002-9311-ccc10c17a95d/image.png)

![](https://velog.velcdn.com/images/yieon/post/fe132dbe-7210-453b-97cb-28a9b57b6c31/image.png)


#### Step2. RDS Cluster Turn on DevOps Guru

1. 적용하고자 하는 RDS에 Tag(Prefix: DevOps-Guru-) 추가

2. 분석 상태 확인
   ![](https://velog.velcdn.com/images/yieon/post/cf0dd030-b0fc-47ed-830a-fc9c2ebd8118/image.png)


#### Step3. Add notifications in DevOps

1. Add notification
   ![](https://velog.velcdn.com/images/yieon/post/39479593-c588-4757-9b8f-a71ab67119ec/image.png)

2. Add Lambda
   ![](https://velog.velcdn.com/images/yieon/post/005a1e60-9404-49ce-a4d6-d4f629af8001/image.png)

3. Lambda Test
   ![](https://velog.velcdn.com/images/yieon/post/140eb16c-2a83-4820-aad6-35d3b7767932/image.png)
