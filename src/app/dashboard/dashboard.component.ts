import { Component } from '@angular/core';
import { FormBuilder,FormGroup } from '@angular/forms';
import {HttpClient} from '@angular/common/http'

@Component({
  selector: 'app-dashboard',
  templateUrl: './dashboard.component.html',
  styleUrls: ['./dashboard.component.css']
})
export class DashboardComponent {
  title = 'pred';
  predictColumn:string=""
  periodicity:string=""
  numbericalValue:string=""
  predicted_result:any

  form: FormGroup;
  private _route: any;
  constructor(public fb: FormBuilder,private http: HttpClient)
  {
    this.form = this.fb.group({
      file: [''],
      duration: [null],
    });
    
   
  // this.upload().subscribe(data =>{
  //   console.log(data)
  // })
  // console.log(this.upload())
  
  
  }
  uploadfile:File|undefined

  onFileSelected(event:any) {
    console.log("file selected")
     this.uploadfile= event.target.files[0];
  }
  // upload():Observable<any>{
  //   let a=this.http.get(
  //     "http://127.0.0.1:5000/summa"
  //   )
  //  console.log(a)
  //  return a
  // }
  submitForm(){
    if(!this.uploadfile){
      alert("File not selected")
      console.log("File not selected")
      
    }
    else{
      console.log(this.periodicity,this.predictColumn,this.numbericalValue)
  var formData: any = new FormData();
    formData.append('file', this.uploadfile);
    formData.append('periodicity', this.periodicity);
    formData.append('predictColumn', this.predictColumn);
    formData.append('numbericalValue', this.numbericalValue);
    
    // formData.append('duration', this.form.get('duration').value);
    this.http
      .post('http://127.0.0.1:5000//getPredictions/', formData)

      
      .subscribe( (result: any)=>{
        // next: (response) => console.log(response),
        
        this.predicted_result=result
        console.log(this.predicted_result)
      });

}
}


}
function subscribe(arg0: (result: any) => void) {
  throw new Error('Function not implemented.');
}



